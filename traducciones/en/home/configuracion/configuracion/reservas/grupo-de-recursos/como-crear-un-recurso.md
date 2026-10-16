---
icon: tennis-ball
origen: 1a2a33c91ad0
---
# How to create a resource

A **resource** is anything that can be booked or assigned to an activity: a court, a pitch or a coach. Resources are grouped by sport (padel, tennis, football…) and they let the system know what's available and when, so bookings can be organised without overlaps.

The club's facilities are usually created during the initial setup. If you need to add a new one, follow these steps.

Follow these steps:

{% stepper %}
{% step %}
### Go to Resource group

* Click the <i class="fa-gear" style="color:blue;">:gear:</i> icon in the top right corner and go to **Settings**.
* Click **Bookings**. The **Resource group** block opens directly.
{% endstep %}

{% step %}
### Create the sport (resource group)

If the sport already exists, go straight to step 4.

* Click <i class="fa-plus-large">:plus-large:</i> to create a new sport or non-sport.
* This window opens. In the example, we create tennis:

<figure><img src="../../../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

These are the required fields:

* **Name:** the name of the sport.
*   **Order:** the position it will appear in on the calendar.

    <figure><img src="../../../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>
* **Sport:** the sport. If you're going to create coaches, choose **No Sport**.
* **Category:** the type of resource.
* **Intervals in minutes:** how many minutes each calendar slot is divided into.
* **Minimum duration:** the shortest a booking can be.
* **Maximum duration:** the longest a booking can be.
{% endstep %}

{% step %}
### Optional sport fields

* **Changes level:** tick it if results in this sport make the player's level go up or down.
* **Calendar cell height:** the height of the calendar slots. The default is 35. To see 4 players in a 1-hour booking with 30-minute slots, we recommend 90.
* **Show players:** tick it to see the players directly on the booking in the calendar.
* **Discontinued:** tick it to stop using this sport.
* **Show participants' initials:** tick it so the display shows initials instead of full names.
* **Maximum time between online bookings:** the smallest free gap allowed between one online booking and another. It stops gaps being left that are so short nobody can book them.
* **Space between bookings at opening/closing:** like the previous one, but also taking into account gaps next to the opening and closing times.
* **Min. time between admin bookings:** the minimum free gap between a booking made from admin and another one.
* **Day start time:** the time the day starts, as a whole number between 0 and 23.
{% endstep %}

{% step %}
### Add the courts (resources)

* Click the **ID** of the sport or non-sport.
*   Go to the **Resources** block.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure></div>
* Click <i class="fa-plus-large">:plus-large:</i>.
* Another window opens:
  * **Name:** the name of the court. Ideally the sport and its number (for example, _Padel 1_). If the court is sponsored, you can use the sponsor's name.
  * **Order:** the position the court will appear in on the calendar.
  * **Court type:** indoor, outdoor, covered, etc.
  * **Surface/wall:** depends on the sport. For tennis or football you choose the surface type; for padel or squash, the wall type.
*   **Save and new:** if you're going to create several courts, use this option. The court is saved and another one opens with almost everything filled in, except the name and order.

    <figure><img src="../../../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

> **Important:** the court won't appear in the calendar yet. First you need to give it a schedule:

[como-crear-un-horario.md](../horarios/como-crear-un-horario.md "mention")
