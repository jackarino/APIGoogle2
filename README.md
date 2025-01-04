# APIGoogle2
APIGoogle2 is a project designed to integrate with the Google Maps API, providing functionality such as geolocation, directions, and place search. The project is divided into two main components: a Flask-based backend and a modern Vite-based frontend.

## Features
- **Backend**: 
  - Built with Python and Flask.
  - Exposes APIs to interact with Google Maps services.
  - Handles requests for geolocation, directions, and place search.

- **Frontend**: 
  - Developed with Vite for a fast and modern web experience.
  - Provides an intuitive user interface for interacting with Google Maps.

## Project Structure
/APIGoogle2
|-- backend/
| |-- venv/ (virtual environment for backend)
| |-- app/ (Flask application files)
| |-- requirements.txt (backend dependencies)
|
|-- frontend/
| |-- frontend-vite/ (frontend source code)
|
|-- README.md (this file)

## Prerequisites
- **Backend**:
  - Python 3.8 or higher
  - Google Maps API key
- **Frontend**:
  - Node.js 16 or higher
  - NPM or Yarn package manager

## Setup Instructions
1.  Navigate to the backend directory
2.  Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate (Linux/Mac)
    venv\Scripts\activate (Windows)
3.  Install dependencies:
    pip install -r requirements.txt
4.  Set up the Google Maps API key as an environment variable:
    export GOOGLE_API_KEY="your_api_key" (Linux/Mac)
    set GOOGLE_API_KEY="your_api_key" (Windows)
5.  Start the Flask server:
    flask run

### Backend
1.  Navigate to the frontend/frontend-vite directory:
2.  Install dependencies:
    npm install
3.  Start the development server:
    npm run dev

### Usage
Access the frontend at http://localhost:5173 (default Vite port).
The backend API runs on http://localhost:5000 (default Flask port).

### Contributing
Feel free to fork the repository and submit pull requests. All contributions are welcome!

### License
APIGoogle2 is licensed under the MIT License.

### Contact
For any questions or feedback, feel free to reach out:  
- **Email**: [franciscoac130@gmail.com](mailto:franciscoac130@gmail.com)  
- **GitHub**: [jackarino](https://github.com/jackarino)  
- **LinkedIn**: [Francisco Muñoz Martín](https://www.linkedin.com/in/francisco-munoz-martin)  

