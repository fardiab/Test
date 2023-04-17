import psycopg2
from django_celery_beat.models import PeriodicTask, PeriodicTasks
from django.shortcuts import get_object_or_404, redirect, render
from core.models import AddInstagram

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from app.tasks import shared_task


@shared_task
def get_instagram(request):
    url = "https://www.instagram.com/"

    driver = webdriver.Chrome("F:\Python\chrome_driver\chromedriver.exe")
    driver.get(url)

    username = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))
    )
    password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))
    )

    username.clear()
    password.clear()
    username.send_keys("turanfutbolclub")
    password.send_keys("Okacover.13")

    WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                'div[class="x9f619 x3nfvp2 xr9ek0c xjpr12u xo237n4 x6pnmvc x7nr27j x12dmmrz xz9dl7a xn6708d xsag5q8 x1ye3gou x80pfx3 x159b3zp xdoji71 x1dejxi8 x9k3k5o xs3sg5q x11hdxyr x12ldp4w x1wj20lx x1dn74xm xif99yt x172qv1o x10djquj x1lhsz42 xzauu7c x1lq5wgf xgqcy7u x30kzoy x9jhf4c"]',
            )
        )
    ).click()
    driver.get("https://www.instagram.com/turanfutbolclub/")
    time.sleep(5)

    ul = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "ul"))
    )
    item = ul.find_elements(By.TAG_NAME, "li")

    follow = item[1].text
    follower = item[2].text

    driver.quit()

    conn = psycopg2.connect(
        host="localhost", database="p_db", user="postgres", password="postgres"
    )

    cur = conn.cursor()

    cur.execute(
        "INSERT INTO follow_counts (follow, follower) VALUES (%s, %s)",
        (follow, follower),
    )
    conn.commit()
    cur.execute("SELECT follow, follower FROM follow_counts ORDER BY id DESC LIMIT 1")
    follow, follower = cur.fetchone()
    cur.close()
    conn.close()

    add_instagram = AddInstagram.objects.create(follower=follower, follow=follow)
    latest_instagram = AddInstagram.objects.latest("id")

    context = {
        "counts": latest_instagram,
    }

    return render(request, "instagram_page.html", context=context)
