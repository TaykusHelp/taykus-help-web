---
icon: display-chart-up-circle-dollar
origen: d2d1d0d733e4
---
# How to set prices for the schedule

In **Calendar prices** you decide the price of each booking according to the day and time. For example, you can charge differently at peak and off-peak times. Each time slot uses a **Service** product, which sets the price.

> **Important:** here you only change **prices**. Court opening and availability don't change. For that, see this article:
>
> <a href="../horarios/como-crear-un-horario.md" class="button primary">How to create a schedule</a>

Follow these steps:

{% stepper %}
{% step %}
### Go to Calendar prices

* Click the <i class="fa-gear" style="color:blue;">:gear:</i> icon in the top right corner and go to **Settings**.
*   Click **Bookings**.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure></div>
*   Click the **Calendar prices** block.<br>

    <figure><img src="../../../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Create the price calendar

* Click :heavy\_plus\_sign:.
*   This window opens:

    <div align="left"><figure><img src="../../../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure></div>

    * **Name:** we recommend it shows the days of the week it includes.
    * **Priority:** a number that decides which price wins if two overlap. The one with the **highest number** applies first. Usually weekdays get the lowest number, the weekend a higher one (so you can apply the weekend price to a weekday) and holidays or closed days the highest.
    * **Start:** the date from which these prices apply. If it's from now, leave it empty.
    * **End:** the date until which they apply. If there's no planned end date, leave it empty.
    * **Day of the week:** tick the days these prices apply on.
* Click **Save**.
{% endstep %}

{% step %}
### Add the price time slots

Within the same day you can have several time slots with different prices (for example, peak and off-peak).

* Click the price calendar's **ID**.
*   Go to the **Prices** block.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (105).png" alt=""><figcaption></figcaption></figure></div>
* Click :heavy\_plus\_sign:.
*   This window opens:

    <figure><img src="../../../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

    * **Resource:** the courts or coaches the price applies to.
    * **Start:** the time the slot starts.
    * **End:** the time the slot ends.
    * **Ends the next day:** tick it if the slot ends at 00:00 or later.
    * **Apply this price to overlaps:** if a booking spans two time slots, the whole booking is charged at this price instead of being split between the two.
    * **Product:** the **Service** product that sets the price for this time slot.
* Click <i class="fa-floppy-disk" style="color:green;">:floppy-disk:</i> to save.
{% endstep %}
{% endstepper %}

> If there are several time slots with different prices, repeat the last step for each one.

## If something doesn't work

* **The booking comes out at €0:** check that the court has been added to the time slot, that the slot covers the booking time and, if it ends at 00:00 or later, that **Ends the next day** is ticked.
* **I've extended the opening hours and it won't let me book the new hours:** also extend the price time slot here. The schedule and the prices must cover the same hours.
* **A public holiday is charged at the normal price:** check that the holiday price calendar has a higher priority than the weekday one.
