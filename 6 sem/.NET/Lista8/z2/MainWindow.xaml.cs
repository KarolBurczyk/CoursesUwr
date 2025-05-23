using System;
using System.Windows;
using System.Windows.Controls;

namespace KółkoKrzyżyk
{
    public partial class MainWindow : Window
    {
        private string currentPlayer = "X";
        private string[,] board = new string[3, 3];

        public MainWindow()
        {
            InitializeComponent();
            ResetGame();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            var button = sender as Button;
            if (button != null && string.IsNullOrEmpty(button.Content?.ToString()))
            {
                button.Content = currentPlayer;
                UpdateBoard(button.Name);

                if (!CheckForWinner())
                {
                    SwitchPlayer();
                }
            }
        }


        private void UpdateBoard(string buttonName)
        {
            if (buttonName == "btn00") board[0, 0] = currentPlayer;
            if (buttonName == "btn01") board[0, 1] = currentPlayer;
            if (buttonName == "btn02") board[0, 2] = currentPlayer;
            if (buttonName == "btn10") board[1, 0] = currentPlayer;
            if (buttonName == "btn11") board[1, 1] = currentPlayer;
            if (buttonName == "btn12") board[1, 2] = currentPlayer;
            if (buttonName == "btn20") board[2, 0] = currentPlayer;
            if (buttonName == "btn21") board[2, 1] = currentPlayer;
            if (buttonName == "btn22") board[2, 2] = currentPlayer;
        }

        private bool CheckForWinner()
        {
            for (int i = 0; i < 3; i++)
            {
                if (board[i, 0] == currentPlayer && board[i, 1] == currentPlayer && board[i, 2] == currentPlayer)
                {
                    EndGame($"Gracz {currentPlayer} wygrał!");
                    return true;
                }
                if (board[0, i] == currentPlayer && board[1, i] == currentPlayer && board[2, i] == currentPlayer)
                {
                    EndGame($"Gracz {currentPlayer} wygrał!");
                    return true;
                }
            }

            if (board[0, 0] == currentPlayer && board[1, 1] == currentPlayer && board[2, 2] == currentPlayer)
            {
                EndGame($"Gracz {currentPlayer} wygrał!");
                return true;
            }

            if (board[0, 2] == currentPlayer && board[1, 1] == currentPlayer && board[2, 0] == currentPlayer)
            {
                EndGame($"Gracz {currentPlayer} wygrał!");
                return true;
            }

            bool isDraw = true;
            foreach (var cell in board)
            {
                if (string.IsNullOrEmpty(cell))
                {
                    isDraw = false;
                    break;
                }
            }

            if (isDraw)
            {
                EndGame("Remis!");
                return true;
            }

            return false;
        }


        private void EndGame(string message)
        {
            txtInfo.Text = message;
            DisableAllButtons();
        }

        private void SwitchPlayer()
        {
            currentPlayer = (currentPlayer == "X") ? "O" : "X";
            txtInfo.Text = $"Teraz gra {currentPlayer}";
        }

        private void DisableAllButtons()
        {
            foreach (var button in GameGrid.Children)
            {
                if (button is Button btn)
                {
                    btn.IsEnabled = false;
                }
            }
        }

        private void ResetGame()
        {
            currentPlayer = "X";
            txtInfo.Text = "Teraz gra X";
            board = new string[3, 3];
            foreach (var button in GameGrid.Children)
            {
                if (button is Button btn)
                {
                    btn.Content = "";
                    btn.IsEnabled = true;
                }
            }
        }
    }
}
