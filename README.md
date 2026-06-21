# VolunTrack: Volunteer Registration System

A robust, responsive web application designed to manage volunteer registrations, track event capacity, and generate administrative reports. Built with **Django**, styled with **Tailwind CSS**, and powered by a **PostgreSQL** database.

##  Features

* **Secure Authentication:** Custom user models handling secure registration, login, and session management.
* **Role-Based Access Control:** Distinct routing and permissions for standard volunteers versus administrative coordinators.
* **Admin Dashboard:** A responsive, Tailwind-styled analytics panel displaying real-time metrics (total volunteers, active events, and database connection status).
* **Event Management:** Tracking for upcoming opportunities with real-time capacity and slot allocation calculations.
* **Automated Reporting:** One-click CSV generation for exporting detailed volunteer registration data.
* **Modern UI:** Clean, mobile-friendly interface using Tailwind CSS and Remix Icons.

##  Tech Stack

* **Backend:** Python, Django (v5+)
* **Database:** PostgreSQL, psycopg2
* **Frontend:** HTML5, Tailwind CSS (via CDN for development), Remix Icons
* **Version Control:** Git, GitHub

##  Local Setup & Installation

Follow these steps to run the project locally on your machine.

### Prerequisites
* Python 3.8+
* PostgreSQL installed and running locally
* Git

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR-USERNAME/volunteer-registration-system.git](https://github.com/YOUR-USERNAME/volunteer-registration-system.git)
cd volunteer-registration-system