
# Weather Information Fetcher with Text-to-Speech

## About

This project fetches the current weather information for a specified location using the WeatherAPI and provides a spoken summary of the weather conditions using the `pyttsx3` text-to-speech library.

## Key Features

- **Weather Data Retrieval**: Fetches current weather data including temperature, weather conditions, humidity, precipitation, and cloud cover.
- **Text-to-Speech Output**: Provides a spoken summary of the weather conditions.
- **Error Handling**: Handles errors gracefully, including network issues and unexpected data formats.

## Technologies and Libraries Used

- **Python**: The programming language used to develop the script.
- **Requests**: For making HTTP requests to the WeatherAPI.
- **Pyttsx3**: For converting text to speech.
- **JSON**: For handling JSON data received from the API.

## Unique Selling Points (USP)

- **Voice-Based Weather Updates**: Delivers weather information audibly, which can be convenient for visually impaired users or those who prefer listening over reading.
- **Real-Time Data**: Provides up-to-date weather information by querying a reliable weather API.
- **User-Friendly**: Simple command-line interface that prompts the user to input their location.

## Setup Instructions

1. **Install Required Libraries**:
    ```bash
    pip install requests pyttsx3
    ```

2. **Configure the API Key**:
    - Replace `api_key` with your WeatherAPI key.

3. **Run the Script**:
    - Execute the script in your Python environment.

## Usage

- The script prompts the user to input their location and then provides a spoken summary of the current weather conditions for that location.
- Ensure you have an active internet connection to fetch the weather data.

## Example

```python
python weather_info.py
```

