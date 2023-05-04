import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class baby_shark_16236_2023_05_04 {

	private int[][] board = new int[21][21];
	private int N;

	private int[] startPoint;
	private final int[][] direction = { {1, 0}, {-1, 0}, {0, 1}, {0, -1}};
	private int sharkSize = 2;
	private int experience = 0;
	private int ans =0;

	public static void main(String[] args) throws IOException {
		baby_shark_16236_2023_05_04 m = new baby_shark_16236_2023_05_04();
		m.init();
		while (true)
			m.findFood();
	}

	private void findFood() {
		int[][] check = new int[21][21];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				check[i][j] = 0;
			}
		}

		check[startPoint[0]][startPoint[1]] = 1;
		ArrayDeque<CustomPoint> dq = new ArrayDeque<>();
		dq.add(new CustomPoint(startPoint, 0));

		ArrayList<int[]> possibleList = new ArrayList<>();
		int stop = -1;

		while (!dq.isEmpty()) {
			CustomPoint pop = dq.pop();
			int x = pop.pointX();
			int y = pop.pointY();
			if (stop != -1 && stop <= pop.level) break;

			for (int i = 0; i < 4; i++) {
				int[] dir = direction[i];
				int next_x = x + dir[0];
				int next_y = y + dir[1];
				if (next_x >= N || next_y >= N || next_x < 0 || next_y < 0) continue;
				if (check[next_x][next_y] == 1) continue;
				if (board[next_x][next_y] > sharkSize) continue;

				check[next_x][next_y] = 1;
				if (board[next_x][next_y] < sharkSize && board[next_x][next_y] != 0) {
					possibleList.add(new int[] {next_x, next_y});
					stop = pop.level + 1;
					continue;
				}
				dq.addLast(new CustomPoint(new int[] {next_x, next_y}, pop.level + 1));
			}
		}

		possibleList.sort(getComparator());

		if (possibleList.isEmpty()) {
			System.out.println(ans);
			System.exit(0);
		}
		startPoint = possibleList.get(0);
		board[startPoint[0]][startPoint[1]] = 0;
		ans += stop;
		experience += 1;
		if (experience == sharkSize) {
			sharkSize += 1;
			experience = 0;
		}
		// printBoard();
	}

	private static Comparator<int[]> getComparator() {
		return (o1, o2) -> {
			if (o1[0] < o2[0])
				return -1;
			if (o1[0] == o2[0] && o1[1] < o2[1])
				return -1;
			return 1;
		};
	}

	private void init() throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		String lines;
		N = Integer.parseInt(reader.readLine());
		for (int i = 0; i < N; i++) {
			lines = reader.readLine();
			board[i] = Arrays.stream(lines.split(" ")).mapToInt(Integer::parseInt).toArray();
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (board[i][j] == 9) {
					startPoint = new int[] {i, j};
					board[i][j] = 0;
				}
			}
		}
		// printBoard();
	}

	private void printBoard() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (i == startPoint[0] && j == startPoint[1])
					System.out.print("$");
				else
					System.out.print(board[i][j]);
			}
			System.out.println();
		}
	}


	static class CustomPoint {
		int[] point;
		int level;

		public CustomPoint(int[] point, int level) {
			this.point = point;
			this.level = level;
		}

		public int pointX () {
			return point[0];
		}

		public int pointY () {
			return point[1];
		}
	}
}
