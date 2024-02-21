# Scan&Carry

Scan&Carry is a web application that scans the text from product images, extracts the ingredients list, provides a description of the ingredients, and gives a health score based on the effect of the ingredients on health.

## Project Setup

### 1. Problem Statement

Scan&Carry aims to solve the challenge of understanding the health implications of the ingredients in our everyday products. It provides an easy way for users to get detailed information about the ingredients just by uploading an image of the product.

### 2. United Nations' Sustainable Development Goals

Scan&Carry aligns with the UN SDG 2: Zero Hunger: If Scan&Carry includes information about food products, it could contribute to this goal by helping users understand the nutritional content of their food and make healthier choices, potentially reducing malnutrition.
In addition to UN SDG 3: Good Health and Well-being, your application, Scan&Carry, could also align with the following United Nations' Sustainable Development Goals:

SDG 12: Responsible Consumption and Production: By providing detailed information about product ingredients, Scan&Carry promotes responsible consumption. Users can make informed decisions about the products they consume, potentially leading to a decrease in the consumption of harmful ingredients.

SDG 13: Climate Action: If Scan&Carry includes information about the environmental impact of certain ingredients or products, it could help raise awareness about climate change and promote more sustainable consumption habits.

!(https://sdgs.un.org/sites/default/files/goals/E_SDG_Icons-13.jpg)

!(https://sdgs.un.org/sites/default/files/goals/E_SDG_Icons-03.jpg) 

!(https://sdgs.un.org/sites/default/files/goals/E_SDG_Icons-12.jpg)

!(https://www.un.org/sites/un2.un.org/files/styles/large-article-image-style-16-9/public/field/image/e_gif_02.gif)

## Implementation

### 3. Architecture

Scan&Carry uses a microservices architecture with the following components:

- OCR Service: Extracts text from uploaded product images
- Ingredient Analysis Service: Analyzes the ingredients and provides a health score
- User Interface: Allows users to upload product images and view the analysis results

### 4. Products and Platforms

Scan&Carry is built using Streamlit for the user interface, Tesseract for OCR, and SQLite for storing ingredient information. It also uses google's gemini vision pro 
for giving a score based on the ingredients idtentified in the product.

## Feedback / Testing / Iteration

### 5. User Feedback and Iteration

(Describe the steps taken to test the solution with real users, the feedback received, what you learned, and the improvements made based on the feedback)

### 6. Code Testing and Iteration

(Describe a coding challenge you faced, how you addressed it, and the technical decisions and implementations you made)

## Success & Completion of Solution

### 7. Solution Success

Scan&Carry successfully provides users with detailed information about product ingredients and their health effects. It uses Google Analytics to track usage metrics. (Provide more details about the success of your solution using metrics, goals, and outcomes)

### 8. Demo Video

(Link to your demo video)

## Scalability

### 9. Future Steps

Future steps for Scan&Carry include expanding the database of ingredients and their health effects, improving the accuracy of the OCR and analysis services, and reaching out to a larger audience through marketing and partnerships.

### 10. Scalability of Technical Architecture

The microservices architecture of Scan&Carry allows it to easily scale to support a larger audience. Each service can be scaled independently based on demand. The application is hosted on Google Cloud Platform, which provides the necessary infrastructure to scale the application.