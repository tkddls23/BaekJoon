import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class set_line_2631_2023_05_04 {

	private List<Integer> students;
	private Integer N;

	public static void main(String[] args) throws IOException {
		set_line_2631_2023_05_04 m = new set_line_2631_2023_05_04();
		m.init();
		m.longestPath();
	}

	private void longestPath() {
		int[] dp = new int[N + 1];
		for (int i = 0; i < N + 1; i++) {
			dp[i] = 0;
		}

		for (int i = 0; i < N; i++) {
			dp[i] = 1;
			Integer currentStudent = students.get(i);
			for (int j = i - 1; j >= 0; j--) {
				Integer beforeStudent = students.get(j);
				if (currentStudent > beforeStudent) {
					dp[i] = Math.max(dp[i], dp[j] + 1);
				}
			}
		}
		int max = Arrays.stream(dp).max().getAsInt();
		System.out.println(N - max);
	}

	private void init() throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.valueOf(reader.readLine());
		students = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			students.add(Integer.valueOf(reader.readLine()));
		}
	}
}
