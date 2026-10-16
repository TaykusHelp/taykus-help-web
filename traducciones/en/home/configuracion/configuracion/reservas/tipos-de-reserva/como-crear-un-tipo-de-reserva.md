---
icon: business-time
origen: a25bf8ff2abf
---
# How to create a booking type

**Booking types** are categories (academy, private lesson, match…) that give each booking its own rules: colour, price, duration, who can book and how. With them:

* You can tell each booking apart at a glance in the calendar by its colour.
* You can see in the reports how many bookings there are of each type.
* You can charge a different price from usual depending on the booking type.

<div align="left"><figure><img src="../../../.gitbook/assets/image (96).png" alt=""><figcaption></figcaption></figure></div>

Follow these steps:

{% stepper %}
{% step %}
### Go to Booking types

* Click the <i class="fa-gear" style="color:blue;">:gear:</i> icon in the top right corner and go to **Settings**.
* Click **Bookings**.\
  ![](<../../../.gitbook/assets/image (97).png>)
*   Click the **Booking types** block.<br>

    <figure><img src="../../../.gitbook/assets/image (98).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Create the booking type

* Click :heavy\_plus\_sign:.
*   This window opens:<br>

    <figure><img src="../../../.gitbook/assets/image (99).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/image (102).png" alt=""><figcaption></figcaption></figure>

> **Important:** fields marked with an asterisk (\*) are required.

#### General details

* **Description (\*):** the name of the booking type.
* **Category:** optional. A subgroup for this type.
* **Order:** the position it appears in on the calendar.
* **Extended description:** optional. Details about this booking type.
* **Image:** optional. Helps you recognise the booking type.

#### Price

* **Price type (\*):** choose from the drop-down:
  * **Per resource:** the price set in the schedules is charged.
  * **Per person:** the schedule price is charged to each participant.
  * **Free:** nothing is charged.
* **Price:** a fixed price for this booking type, ignoring the calendar prices.
* **Booking per place:** tick it only if the price type is **Per person**.

#### Online booking and cancellation

* **Is public:** tick it so it can be booked online.
* **Allows online cancellation:** if it's on, players can cancel online. If not, only the club can cancel.
* **Minimum minutes in advance:** the minimum notice required to book.
* **Maximum minutes in advance:** the maximum notice allowed to book.
* **Minutes in advance for cancellations:** how many minutes beforehand bookings can be cancelled.
* **Pre-booking minutes:** the minutes the court is held while the player finishes booking.
* **Hours before it expires:** how many hours before the booking it expires if it isn't completed.
* **Refund payment on cancellation and expiry:** tick it so the player gets their money back if the booking is cancelled or expires without being completed.

#### Participants and level

* **Minimum number of participants (\*):** the minimum number of people for this booking type.
* **Maximum number of participants (\*):** the maximum number of people.
* **Minimum level** and **maximum level:** the playing level allowed.
* **Gender:**
  * **Male:** only male users can book.
  * **Female:** only female users can book.
  * **Open:** anyone can book.

#### Limits

* **Allow custom duration:** lets you change the end time when creating the booking from admin.
* **Maximum number of bookings per day:** how many bookings of this type can be made per day.
* **Maximum number of bookings:** if there's a maximum advance time, it counts bookings from today up to that time. If not, it counts all bookings from today.
* **Maximum online and admin booking restrictions:** the limits apply to both online bookings and the club's own bookings.

#### Appearance

* **Colours:** the colour of this booking type in the calendar. It can be fixed or change depending on the booking status.
{% endstep %}

{% step %}
### Add the resources

* In **Booking types**, click the **ID** of the type you've just created.
*   Open the **Resources** tab.

    <figure><img src="../../../.gitbook/assets/image (103).png" alt=""><figcaption></figcaption></figure>
* Click :heavy\_plus\_sign:.
*   This window opens:<br>

    <figure><img src="../../../.gitbook/assets/image (104).png" alt=""><figcaption></figcaption></figure>

    * **Resource group:** the resource this booking type takes up.
    * **Minutes blocked before the booking:** how many minutes beforehand the resource is blocked to get it ready. For example, if the booking starts at 10:00 and you enter 10 minutes, the court is blocked from 9:50.
    * **Duration:** the booking's default duration.
    * **Allowed durations:** the durations that can be chosen, in minutes and separated by spaces (for example: `30 60 120`). If you leave it empty, they're calculated from the resource group settings.
    * **Primary resource:** the resource chosen first.
    * **Selectable online:** tick it so the player can choose this resource when booking online.
* Click **Save**.

> If the booking type takes up two resources (for example, court and coach), repeat this step for each one.
{% endstep %}
{% endstepper %}

## If something doesn't work

* **The booking type doesn't appear when booking a court:** add that court in the booking type's **Resources** tab (step 3).
