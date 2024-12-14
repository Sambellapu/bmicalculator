# BMI Report Visualization (GUI Python)

This repository contains a Python program that generates a BMI (Body Mass Index) report on a scale, providing a clear visualization of the user's BMI category. The program uses colors to indicate health status: 
- **Red**: Underweight or Overweight
- **Green**: Healthy (Normal weight)

## Features

- **BMI Calculation**: Accepts user input for height and weight to calculate BMI.
- **Categorized Report**: Displays whether the user is underweight, normal, or overweight.
- **Color Coding**: Uses:
  - **Red** for Underweight and Overweight.
  - **Green** for Normal weight.
- **Interactive BMI Scale**: Displays BMI position dynamically on a scale using the `.set()` method.

## Requirements

- Python 3.x
- tkinter (Standard Python library for GUI development)

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bmi-report-visualization.git
   cd bmi-report-visualization
   ```
2. Run the program:
   ```bash
   python bmi_report.py
   ```

## Usage

1. **Input Details**:
   - Enter your height (in meters) and weight (in kilograms).

2. **View Report**:
   - The program calculates and displays your BMI.
   - A visual scale indicates your BMI category (Underweight, Normal, or Overweight).

3. **Interpret Colors**:
   - **Red**: Underweight or Overweight.
   - **Green**: Normal weight.

## Example

Here is an example of how the program works:

```
Enter your height (m): 1.75
Enter your weight (kg): 70

BMI: 22.9
Category: Normal weight

[----------|***GREEN***|-----------]
```

## Program Details

- **BMI Categories**:
  - Underweight: BMI < 18.5
  - Normal weight: BMI 18.5 - 24.9
  - Overweight: BMI > 24.9

- **Visualization**:
  - Uses the `.set()` method in `tkinter` to dynamically update a scale representing BMI.

## Future Improvements

- Add more detailed health recommendations based on BMI.
- Include support for imperial units (feet, inches, pounds).
- Provide graphical analytics for BMI trends over time.
- Create a mobile-friendly version.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Health organizations for BMI classification standards.
- Python community, for the tools and resources.

---

Stay Healthy! 🩺


