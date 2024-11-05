# Chocolate House Application

## Description
This application manages the following for a fictional chocolate house:
- Seasonal flavor offerings
- Ingredient inventory
- Customer flavor suggestions and allergy concerns

## Requirements
- Docker

## Setup and Run Instructions

1. Clone the repository:
    ```bash
    git clone <repo_url>
    cd chocolate_house
    ```

2. Build and run the Docker container:
    ```bash
    docker build -t chocolate_house .
    docker run -p 5000:5000 chocolate_house
    ```

## API Endpoints

- **Add Seasonal Flavor**: `POST /flavors`
    - **Body**:
      ```json
      {
        "flavor_name": "Pumpkin Spice",
        "availability": "Fall"
      }
      ```

- **Add Ingredient**: `POST /ingredients`
    - **Body**:
      ```json
      {
        "ingredient_name": "Cocoa Powder",
        "quantity": 100
      }
      ```

- **Add Customer Suggestion**: `POST /suggestions`
    - **Body**:
      ```json
      {
        "customer_name": "John Doe",
        "flavor_suggestion": "Mint Chocolate",
        "allergy_concern": "None"
      }
      ```

## Testing
Use `curl` commands to test each endpoint, or test with Postman.

## Edge Cases
- Duplicate entries should not be allowed for unique items (like flavor names or ingredient names).
- Invalid data (like negative quantities) should be handled gracefully.


## Running the Application in Docker

### Build the Docker Image

1. Run this command to build the Docker image:
 
   docker build -t chocolate_house_app .



Run the Docker Container
Start the container and expose port 5000:


docker run -p 5000:5000 chocolate_house_app