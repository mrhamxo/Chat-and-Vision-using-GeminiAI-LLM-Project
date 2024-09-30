# Chat & Vision using GeminiAI LLM Project Application

## Project Summary
The **Gemini Application** is a versatile Streamlit-based web application that utilizes Google's Gemini LLM for two main functionalities: a Chat interface and an Image Analysis interface. Users can interact with the application by asking questions or uploading images, receiving intelligent responses powered by generative AI.

## Objectives
- **Chat Functionality**: Allow users to ask questions and receive informative responses through natural language processing.
- **Image Analysis**: Enable users to upload images and receive descriptive insights based on the uploaded content.
- **User-friendly Interface**: Provide an intuitive and engaging user experience using Streamlit's interactive features.

## Workflow
1. **Setup**: 
   - Ensure all dependencies are installed, including Streamlit and the Google Generative AI library.
   - Set up the environment variables for Google API key using a `.env` file.
  
2. **Running the Application**:
   - Launch the application using the command:
     ```
     streamlit run app.py
     ```
     
3. **User Interaction**:
   - **Chat Mode**:
     - Users can enter a question in the provided text input.
     - Click the "Ask the question" button to receive a response from the Gemini LLM.
   - **Vision Mode**:
     - Users can enter an input prompt and upload an image.
     - Click the "Tell me about the image" button to analyze the image and receive insights.

## Sreenshot User Interface
![chat](https://github.com/user-attachments/assets/86963007-6d98-4ab8-81fb-5d22a7b8029a)
![vision](https://github.com/user-attachments/assets/04e802c4-34c5-4567-86bc-56cefbd96f83)

## Conclusion
The Gemini Application demonstrates the capabilities of generative AI in enhancing user interactions through natural language processing and image analysis. By integrating both functionalities into a single application, users can seamlessly switch between chat and vision tasks, exploring the potential of AI in real-world scenarios.

## Future Work
- **Enhancements**: Improve the natural language understanding and image analysis capabilities by fine-tuning the models.
- **Additional Features**: Implement more advanced functionalities such as voice input/output and support for more file types in the image analysis.
- **User Feedback**: Gather user feedback to refine the application and introduce features that enhance usability and engagement.
