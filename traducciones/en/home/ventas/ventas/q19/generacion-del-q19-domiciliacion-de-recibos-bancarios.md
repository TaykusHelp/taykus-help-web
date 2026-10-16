---
icon: money-bill-transfer
origen: 7c1bb276cf94
---
# Generating the Q19 (direct debit of bank receipts)

In this article we'll see how to create a **Q19** file to manage fee remittances, how to add the lines and what to check before closing and downloading it.

Here's an explainer video that takes you through it step by step:

### Explainer video

{% embed url="https://youtu.be/IA2_rz0yjHM" %}

In this article we explain how to do this:

### Before you start

Before generating a Q19, check that the following details have been created in:

* **Settings > Sales > Companies**

To find out how, you can read the following article:

* [antes-de-empezar-a-remesar.md](antes-de-empezar-a-remesar.md "mention")

{% stepper %}
{% step %}
### Go to the Q19 section

* Go to the left-hand menu and select **Sales.**
* Click **Q19**.
*   From this section you can see the remittances already created or generate a new one.<br>

    <figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Create a new Q19 file

Once you're in **Q19**, press the **add** button to create a new file.

Then fill in the main fields:

* **Description**: enter a name to identify the remittance.\
  Example: **MEMBER FEES REMITTANCE APRIL 2026**
* **Issuer ID**: select the issuer.
*   **Comments**: this field is optional.<br>

    <figure><img src="../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

When you've filled in the information, press **Save**.
{% endstep %}

{% step %}
### Add the lines to the Q19

*   Once the file has been saved, go to the **Q19 Lines** section and press the **+** button to add the lines that will be included in the remittance.<br>

    <figure><img src="../../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>
*   A window opens with the **Sales lines**, where you can easily find the fees that need to be included in the file.<br>

    <figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Filter the lines correctly

To find only the lines that should be part of the remittance, it's important to apply the right filters.

* #### Ticket status
  * Filter by **Pending** to show only the lines that haven't been processed yet.
* #### Due date
  * Use this filter to find the fees for the period you want to include in the remittance.
* #### Product type
  * Filter by **Member Fees**, so that only member fee lines appear and not other products or bookings.

Once the filters are applied, select the lines you want to include and press **Select**.
{% endstep %}

{% step %}
### Check for errors

When you select the lines in the previous step, an **Error** warning may appear; select **OK** and check those errors.

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

*   In the same Q19 file you'll also find the **Errors** tab.<br>

    <figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>
* This tab lets you spot problems before closing the remittance. If any line shouldn't be included or has a problem, check it before continuing and select Discard.
* You can also remove lines you've added from the Q19 itself if you need to correct your selection.
{% endstep %}

{% step %}
### Review the lines added

*   When you go back to the Q19 file, you'll see the lines added in the **Lines** section.<br>

    <figure><img src="../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>
* From here you can check information such as:
  * **Player**
  * **Account holder**
  * **Description**
  * **Amount**
* It's important to check that the lines included are correct before continuing.
{% endstep %}

{% step %}
### Close the Q19 file

* When you've checked that all the lines are correct, click Close.
* The program shows a notice with the total amount and number of payments.\
  ![](<../../.gitbook/assets/image (19).png>)
* Click **OK.**
* Once done, the file's status changes to **Closed.**
* This step is essential to get the file ready correctly.
{% endstep %}

{% step %}
### Download the file

*   When the Q19 status is **Closed**, you can use the **Download** option to get the generated file.<br>

    <figure><img src="../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>
* This is the file you'll use to manage the remittance and upload to the bank.
{% endstep %}
{% endstepper %}

Before closing and downloading the file, remember to check that the lines included are for the right period, that they belong to the **Member Fees** product type and that there are no problems in the Errors tab.

This way, you can generate the Q19 file correctly with the lines that should be included in the remittance.
