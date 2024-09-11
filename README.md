# 📚 LittleTreasures_back

## Table of Contents
- [📄 Project Description](#-project-description)
- [🎯 Motivation](#-motivation)
- [🚀 Features](#-features)
- [📅 Project Management](#-project-management)
- [📖 Documentation](#-documentation)
- [🛠 Technologies Used](#-technologies-used)
- [📦 Installation and Configuration](#-installation-and-configuration)
- [🧪 Testing](#-testing)
- [🤝 Contributions](#-contributions)
- [📧 Contact](#-contact)



## 📄 Project Description

**LittleTreasures**  a responsive application. An app to view the events organized by the kindergarden, where parents, once registered, can sign their children up for the event.:

## 🎯 Motivation

My motivation is to offer a clean and accessible design for the user with the possibility to interact intuitively with the application.

## 🚀 Features

### LittleTreasures Users (CRUD Operations)
- **Create**: Register new users in the application.
- **Read**: Search and browse itineraries by different criteria.
- **Validation**: Ensure there are no duplicates in the itineraries by using appropriate validations.
- **Update**: The system updates the user's data.
- **Delete**: Remove users from the system.

### User´s childrens (CRUD Operations)
- **Create**: Register new child in the application.
- **Read**: Search you child in your profile
- **Validation**: Ensure there are no duplicates in the itineraries by using appropriate validations.
- **Update**:  The user updates the user's children.
- **Delete**: Remove user's child from the system.

### Events (CRUD Operations - Only admin)
- **Create**: Register new events in the application.
- **Read**: You can view created events and explore the information
- **Update**: You can update events
- **Delete**: Events can be deleted

### Events (CRUD Operations)
- **Read**: You can view created events and explore the information


## 📅 Project Management
This project is an individual work. Tools such as Jira were used for backlog management and sprint planning.


## 🛠 Technologies Used


- **Language**: Python (v3.12.4)
- **Database**: PostgreSQL (v16.2)
- **Testing**: Jest (v29.7)
- **Version Control**: Git (v2.45.2) with GitFlow
- **IDE**: Visual Studio Code
- **Frameworks**: React
- **Design Tool**: Figma
- **Framework Backend:**: Django (v5.1.1)
- **API Development:**: Django Rest Framework (v3.15.2)


## 📦 Installation and Configuration

1. **Clone the repository:**
   ```bash
   git clone
   https://github.com/Erieltxu/LittleTreasures_back.git
   ```
2. **Create and activate your virtual enviroment:**
    ```bash
    python -m venv env
    env\Scripts\activate
    ```
    
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Configure the database:**
 Create a database in PostgreSQL with same name the proyect. Add to settings.py:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nameBBDD',
        'USER': 'your BBDD user',
        'PASSWORD': 'your BBDD password',
        'HOST': 'localhost', #(usually is the same)
        'PORT': '5432' #(usually is the same)
    }
} 
   ```
5. **Perform the migrations and run server:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
   
## 🧪 Testing

- **Run integration tests:**

    ```bash
    Pytest
    ```
- Use Gherking test: Given, When Then
    ```bash
        """
        Given valid user data
        When registering a new user
        Then the user should be created
        And a 201 status code should be returned
        """
    ```

## 📧 Contact

For any inquiries, you can reach out to us through our GitHub and LinkedIn profiles:

- [![GitHub Octocat](https://img.icons8.com/ios-glyphs/30/000000/github.png)](https://github.com/Erieltxu)  [![LinkedIn](https://img.icons8.com/ios-glyphs/30/0077b5/linkedin.png)](https://www.linkedin.com/in/leire-del-hoyo-aldecoa) Leire 

## 😊 If you've made it this far, feel free to follow me on GitHub or LinkedIn. I'd love to stay in touch!