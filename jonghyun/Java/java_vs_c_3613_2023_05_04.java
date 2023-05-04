import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;
import java.util.stream.Collectors;

public class java_vs_c_3613_2023_05_04 {
	
	private String input;
	private boolean java = false;
	private boolean c = false;

	public static void main(String[] args) {
		java_vs_c_3613_2023_05_04 m = new java_vs_c_3613_2023_05_04();
		m.init();
		m.checkType();
		if (m.c)
			System.out.println(m.changeJava());
		else
			System.out.println(m.changeC());
	}

	private String changeC() {
		List<Integer> charList = input.chars().boxed()
			.collect(Collectors.toList());
		ListIterator<Integer> iterator = charList.listIterator();


		while (iterator.hasNext()) {
			Integer next = iterator.next();
			if (next >= 65 && next <= 90) {
				iterator.remove();
				iterator.add((int)'_');
				iterator.add(next + 32);
			}
		}
		return getString(charList);
	}

	private String changeJava() {
		List<Integer> charList = input.chars().boxed()
			.collect(Collectors.toList());
		ListIterator<Integer> iterator = charList.listIterator();

		while (iterator.hasNext()) {
			Integer next = iterator.next();
			if (next == (int)'_') {
				iterator.remove();
				Integer next2 = iterator.next();
				iterator.remove();
				iterator.add(next2 - 32);
			}
		}

		return getString(charList);
	}

	private static String getString(List<Integer> charList) {
		StringBuilder sb = new StringBuilder();
		for (int ch: charList) {
			sb.append((char)ch);
		}
		return sb.toString();
	}

	private void checkType() {
		boolean isJava = false;
		boolean isC = false;

		boolean before_ = false;
		// 자바인지 C인지 확인
		for (int i = 0; i < input.length(); i++) {
			char c = input.charAt(i);
			if (c == '_') {
				// _는 연속되면 안됨.
				if (before_) {
					System.out.println("Error!");
					System.exit(0);
				}
				before_ = true;
				isC = true;
			} else if (c >= 65 && c <= 90) {
				isJava = true;
				before_ = true;
			} else {
				before_ = false;
			}
		}

		// 마지막 문자가 '_'인지 확인
		if (input.charAt(input.length()-1) == '_') {
			isJava = true;
			isC = true;
		}

		// 맨 앞이 대문자이거나 _인지 확인
		char first = input.charAt(0);
		if ((first >= 65 && first <= 90 ) || (first == '_') ) {
			isJava = true;
			isC = true;
		}

		// 둘 다 true가 아닌 경우만 패스
		if ( !(isJava && isC) ) {
			java = isJava;
			c = isC;
		} else {
			System.out.println("Error!");
			System.exit(0);
		}
	}

	private void init() {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		try {
			input = reader.readLine();
		} catch (IOException e) {
			
		}
		
	}
}
