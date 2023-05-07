
import string
def the_helper(s):
	stack = []
	for i in s:
		stack.append(i)
	s = ""
	while stack:
		s += stack.pop()
	return s

if __name__ == "__main__":
	str = "Vishal"
	reversed_str = the_helper(str)
	print("Reversed string is: ", reversed_str)
