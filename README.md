# BMI-Calculator-Project

This is a simple Django-based web application that allows users to calculate their Body Mass Index (BMI). The application takes user inputs for height and weight and returns the calculated BMI along with a health classification.

## Features

- **Input Form:** Users can enter their height (in cm) and weight (in kg).
- **BMI Calculation:** The application computes the BMI based on the input values.
- **Health Classification:** The BMI result is classified into categories like underweight, normal weight, overweight, etc.
- **Responsive Design:** The application is responsive and works well on various devices.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine
- `pip` (Python package installer) is installed
- `virtualenv` is installed (optional but recommended)

## Installation

Follow these steps to get the project up and running:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MatthiasKCM/BMI-Calculator-Project.git
   cd BMI-Calculator-Project
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for accessing the Django admin):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000` to start using the BMI Calculator.

## Usage

- **Calculate BMI:** Enter your height and weight into the provided form, then click "Calculate". The application will display your BMI along with a classification.
- **Admin Panel:** Access the Django admin panel at `http://127.0.0.1:8000/admin` (if you created a superuser).

## Deployment

To deploy this application to a production environment, you may consider using services like Heroku, AWS, or any other web hosting provider that supports Django. Ensure to set up the necessary environment variables and use a production-ready database (e.g., PostgreSQL).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.




