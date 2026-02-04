#include <iostream>
#include <vector>

using namespace std;

const int N = 9;

void printBoard(vector<vector<int>>& board) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

pair<int, int> findEmpty(vector<vector<int>>& board) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (board[i][j] == 0) {
                return {i, j};
            }
        }
    }
    return {-1, -1};
}

bool isValid(vector<vector<int>>& board, int num, pair<int, int> pos) {
    int row = pos.first;
    int col = pos.second;

    // Check row
    for (int j = 0; j < N; j++) {
        if (board[row][j] == num && j != col) {
            return false;
        }
    }

    // Check column
    for (int i = 0; i < N; i++) {
        if (board[i][col] == num && i != row) {
            return false;
        }
    }

    // Check 3x3 box
    int boxRow = row / 3;
    int boxCol = col / 3;

    for (int i = boxRow * 3; i < boxRow * 3 + 3; i++) {
        for (int j = boxCol * 3; j < boxCol * 3 + 3; j++) {
            if (board[i][j] == num && (i != row || j != col)) {
                return false;
            }
        }
    }

    return true;
}

bool solveSudoku(vector<vector<int>>& board) {
    pair<int, int> empty = findEmpty(board);

    if (empty.first == -1) {
        return true;
    }

    int row = empty.first;
    int col = empty.second;

    for (int num = 1; num <= 9; num++) {
        if (isValid(board, num, {row, col})) {
            board[row][col] = num;

            if (solveSudoku(board)) {
                return true;
            }

            board[row][col] = 0;
        }
    }

    return false;
}

int main() {
    vector<vector<int>> board(N, vector<int>(N));

    // Read input
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> board[i][j];
        }
    }

    if (solveSudoku(board)) {
        printBoard(board);
    } else {
        cout << "No solution exists" << endl;
    }

    return 0;
}