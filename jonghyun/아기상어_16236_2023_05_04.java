import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class 아기상어_16236_2023_05_04 {

	private int[][] board = new int[21][21];
	private int N;

	public static void main(String[] args) throws IOException {
		아기상어_16236_2023_05_04 m = new 아기상어_16236_2023_05_04();
		m.init();

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
			Arrays.stream(board[i]).forEach(System.out::print);
			System.out.println();
		}
	}
}
