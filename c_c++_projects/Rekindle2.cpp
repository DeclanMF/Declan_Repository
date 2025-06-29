#include <iostream>
#include <vector>
#include <string>
#include <chrono>    // For std::chrono::milliseconds
#include <thread>    // For std::this_thread::sleep_for
#include <random>    // For random number generation
#include <conio.h>   // For _kbhit() and _getch() on Windows
#include <windows.h> // For console functions on Windows

// --- Console Utility Functions (Windows specific) ---

// Function to set cursor position
void gotoxy(int x, int y)
{
    COORD coord;
    coord.X = x;
    coord.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

// Function to hide the console cursor
void hideCursor()
{
    CONSOLE_CURSOR_INFO cursorInfo;
    GetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &cursorInfo);
    cursorInfo.bVisible = FALSE; // Set the cursor visibility to false
    SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &cursorInfo);
}

// Function to clear the console screen
void clearScreen()
{
    // This is a simple way to clear the screen, but might flicker.
    // For more robust clearing, you'd calculate and fill the console buffer.
    system("cls"); // For Windows
    // For Linux/macOS: system("clear");
}

// --- Game Constants ---
const int GAME_WIDTH = 25;  // Width of the road
const int GAME_HEIGHT = 20; // Height of the game area

// --- Game Structures ---
struct Car
{
    int x, y;
    char symbol;
};

// --- Global Game Variables ---
Car playerCar;
std::vector<Car> obstacles;
int score = 0;
int gameSpeed = 200; // Milliseconds delay per frame (smaller = faster)
bool gameOver = false;

// --- Game Functions ---

void initializeGame()
{
    playerCar = {GAME_WIDTH / 2, GAME_HEIGHT - 2, 'A'}; // Player car in the middle, near bottom
    obstacles.clear();
    score = 0;
    gameSpeed = 200;
    gameOver = false;
    clearScreen();
    hideCursor();

    // Draw game boundaries
    for (int i = 0; i < GAME_HEIGHT; ++i)
    {
        gotoxy(0, i);
        std::cout << '|';
        gotoxy(GAME_WIDTH + 1, i);
        std::cout << '|';
    }
    gotoxy(0, GAME_HEIGHT);
    for (int i = 0; i <= GAME_WIDTH + 1; ++i)
    {
        std::cout << '-';
    }
}

void draw()
{
    // Clear only the game area for redraw
    for (int y = 0; y < GAME_HEIGHT; ++y)
    {
        for (int x = 1; x <= GAME_WIDTH; ++x)
        {
            gotoxy(x, y);
            std::cout << ' '; // Clear previous characters
        }
    }

    // Draw player car
    gotoxy(playerCar.x, playerCar.y);
    std::cout << playerCar.symbol;

    // Draw obstacles
    for (const auto &obs : obstacles)
    {
        gotoxy(obs.x, obs.y);
        std::cout << obs.symbol;
    }

    // Display score
    gotoxy(GAME_WIDTH + 5, 2);
    std::cout << "Score: " << score << "     "; // Spaces to clear old score
}

void processInput()
{
    if (_kbhit())
    {                        // Check if a key has been pressed
        char key = _getch(); // Get the pressed key (non-blocking)
        if (key == 'a' || key == 'A' || key == 75)
        { // 'a' or Left Arrow (ASCII 75)
            if (playerCar.x > 1)
            { // Ensure car stays within left boundary
                playerCar.x--;
            }
        }
        else if (key == 'd' || key == 'D' || key == 77)
        { // 'd' or Right Arrow (ASCII 77)
            if (playerCar.x < GAME_WIDTH)
            { // Ensure car stays within right boundary
                playerCar.x++;
            }
        }
        else if (key == 27)
        { // Escape key
            gameOver = true;
        }
    }
}

void updateGame()
{
    // Move existing obstacles down
    for (size_t i = 0; i < obstacles.size();)
    {
        obstacles[i].y++;
        if (obstacles[i].y >= GAME_HEIGHT)
        {
            // Remove obstacle if it goes off screen and reward score
            obstacles.erase(obstacles.begin() + i);
            score += 10;
            // Gradually increase speed
            if (gameSpeed > 50 && score % 50 == 0)
            { // Increase speed every 50 points
                gameSpeed -= 5;
            }
        }
        else
        {
            i++;
        }
    }

    // Generate new obstacles randomly
    static std::random_device rd;
    static std::mt19937 gen(rd());
    static std::uniform_int_distribution<> dis(1, GAME_WIDTH); // X position for new obstacle

    // Adjust obstacle creation frequency based on speed
    static int obstacleSpawnCounter = 0;
    int spawnFrequency = (gameSpeed < 100) ? 10 : 20; // Spawn more frequently when faster

    if (++obstacleSpawnCounter >= spawnFrequency)
    { // Spawn new obstacle every X frames
        obstacles.push_back({dis(gen), 0, 'X'});
        obstacleSpawnCounter = 0;
    }

    // Check for collisions
    for (const auto &obs : obstacles)
    {
        // Check if player car and obstacle occupy the same space
        if (playerCar.x == obs.x && playerCar.y == obs.y)
        {
            gameOver = true;
            break;
        }
        // Simple collision for car being slightly wider or higher (adjust based on symbol size)
        // If your 'A' is 1 char wide and 'X' is 1 char wide, exact match is fine.
        // For larger "cars" you'd check bounding boxes.
    }
}

void showGameOver()
{
    clearScreen();
    gotoxy(GAME_WIDTH / 2 - 5, GAME_HEIGHT / 2 - 2);
    std::cout << "GAME OVER!";
    gotoxy(GAME_WIDTH / 2 - 8, GAME_HEIGHT / 2);
    std::cout << "Final Score: " << score;
    gotoxy(GAME_WIDTH / 2 - 10, GAME_HEIGHT / 2 + 2);
    std::cout << "Press 'r' to Restart or 'q' to Quit";

    char choice;
    do
    {
        choice = _getch();
    } while (choice != 'r' && choice != 'R' && choice != 'q' && choice != 'Q');

    if (choice == 'r' || choice == 'R')
    {
        initializeGame();
        // The main game loop will be called again after this returns
    }
    else
    {
        // Exit the program
        exit(0);
    }
}

int main()
{
    // Set console title
    SetConsoleTitleA("C++ Console Car Game");

    while (true)
    {
        initializeGame();
        while (!gameOver)
        {
            processInput();
            updateGame();
            draw();
            std::this_thread::sleep_for(std::chrono::milliseconds(gameSpeed));
        }
        showGameOver();
    }

    return 0;
}