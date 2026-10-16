---
icon: clock-three
origen: 15104b307bfc
---
# How to create a schedule

Courts and coaches only appear in the calendar when they have a schedule. The schedule sets which days and at what times each resource is open, and how it can be booked.

Taykus comes with two schedules already created. You can change or delete them and create a new one. In this article we explain how to create one from scratch.

### Explainer video

{% embed url="https://youtu.be/0UDRdOUjr54" %}

Follow these steps:

{% stepper %}
{% step %}
### Go to Schedules

* Click the <i class="fa-gear" style="color:blue;">:gear:</i> icon in the top right corner and go to **Settings**.
*   Click **Bookings**.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure></div>
*   Click the **Schedules** block.<br>

    <div align="left"><figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
### Create the schedule

* Click :heavy\_plus\_sign:.
*   This window opens:<br>

    <div align="left"><figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure></div>

    * **Name:** a name based on the days it includes (for example, _Weekdays_ or _Weekend_).
    * **Priority:** which one wins if two schedules overlap: the **highest number** wins. Usually the weekend gets a higher priority than weekdays: that way, if you want a weekday public holiday to work like a Saturday, that day will use the weekend schedule.
    * **Start/End:** the dates from and to which the schedule applies. If you leave them empty, it applies from when you save it.
    * **Day of the week:** tick the days this schedule includes.
* Click **Save**.
{% endstep %}

{% step %}
### Open the opening hours

* When you save, the schedule opens on the **Dates** tab.
*   Click the **Opening hours** tab.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure></div>

Here you'll set up two things:

* **Opening and closing:** which facilities (padel, tennis, football…) follow this schedule and what time they open and close.
* **Intervals and duration of online bookings:** how often players can book online (every 30, 60 or 90 minutes) and the minimum and maximum duration of bookings.

> **Important:**
>
> * If the club has an academy, also add the **coaches** to the schedule.
> * You can create as many schedules as you need. If all the facilities open at the same time, put them in a single schedule; if each one has its own, create one for each.
{% endstep %}

{% step %}
### Add the opening hours

* Click :heavy\_plus\_sign:.
*   This window opens:<br>

    <figure><img src="../../../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

    * **Resource:** all the courts or coaches this schedule applies to.
    * **Start:** opening time.
    * **End:** closing time.
    * **Ends the next day:** tick it if the schedule ends at 00:00 or later.
    * **Intervals in minutes:** how many minutes each calendar slot is divided into. For example, with 30 minutes you'll see slots at 09:00, 09:30, 10:00, 10:30…
    * **Minimum duration:** the shortest a booking can be. It can't be less than the interval and must be a multiple of it.
    * **Maximum duration:** the longest a booking can be. It must be a multiple of the interval.
* Click **Save**.
{% endstep %}
{% endstepper %}

## If something doesn't work

* **The court doesn't appear in the calendar:** check that it's been added in **Opening hours** (step 4). Creating the schedule without adding the court isn't enough.
* **I've extended the schedule and it won't let me book the new hours:** also extend the time slot in [calendar prices](../precios-por-calendario/como-poner-precios-al-horario.md). The schedule and the prices must cover the same hours.
* **It won't let me save the duration:** the minimum and maximum duration must be multiples of the interval. With a 30-minute interval you can enter 60 or 90, but not 45.
