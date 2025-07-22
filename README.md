# Indian States and UTs Guessing Game

A fun, interactive Turtle graphics-based game to test your knowledge of the states and union territories (UTs) of India. This game displays a blank map of India, and the player guesses the names of the states. Each correct guess is labeled on the map, while missed states can be saved for later learning.

## Features

- **Clickable Prompt:** Enter the names of Indian states/UTs to guess their locations.
- **Live Feedback:** Correct guesses are labeled on the map at precise coordinates.
- **Educational:** Missed states are saved in a CSV file for further study.
- **Replayability:** See your progress and try to complete all entries.


### Prerequisites

- Python 3.x
- `pandas` package
- `turtle` module (present in the standard Python library)

### Files Included

- `main.py`: Main game script.
- `India-States-UTs.csv`: CSV file containing state names and their coordinates.
- `India.gif`: Map image used as the game background.
- `India.jpg`: (Optional) Preview image for the README.

### Setup Instructions

1. **Clone this repository** or download the files to your local machine.
2. **Add Map Image:** Ensure `India.gif` (a blank map outline) is present in your working directory.
3. **Install required packages:**  
   ```bash
   pip install pandas
   ```

4. **Run the game:**  
   ```bash
   python main.py
   ```

## How to Play

1. A map of India appears with no state names.
2. Enter the name of a state or UT in the prompted dialog box.
   - The game is not case-sensitive but expects correct spelling.
3. Correct guesses are displayed on the map.
4. Type `Exit` anytime to quit and save a list of missed states in `states_to_learn.csv`.
5. Try to guess all 28 states to complete the game!

## Files Overview

| File                    | Description                                            |
|-------------------------|--------------------------------------------------------|
| `main.py`               | Main game logic with prompts and map interaction       |
| `India-States-UTs.csv`  | States/UTs names alongside their coordinates           |
| `India.gif`             | Blank map outline image used in Turtle graphics        |
| `states_to_learn.csv`   | (Auto-generated) List of unguessed states/UTs          |

## Customization

- **Add More States/UTs:** Edit `India-States-UTs.csv` to add more entries or adjust coordinates.
- **Change Map Image:** Replace `India.gif` with another map using the same coordinate system.

## License

This project is for educational and personal, non-commercial use.

## Contributing

Pull requests and suggestions are welcome! Please ensure changes to the map or coordinates are reflected in both the code and CSV file.

Enjoy learning India’s geography while having fun!

## Author

- [Subham Nayak](https://github.com/Subham73-cmd)
