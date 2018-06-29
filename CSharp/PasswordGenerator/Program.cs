using System;
using System.Collections.Generic;

namespace PasswordGenerator
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			Main:
			int PassLen;
			bool UpCheck, NumCheck, SpecCheck, GenAgain;
			string reqType, FinalPass;
			List <char> alph = new List<char> {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}; 
			List <char> alphUpper = new List<char> {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
			List <char> spec = new List<char> { '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '<', '>', '?' };
			List <char> num = new List<char> { '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' };

			Console.WriteLine ("Welcome to the Password Generator");
			Console.WriteLine ("----------------------------------");
			Console.WriteLine ("Total Password Length (must be at least 6 characters):");
			reqType = "total password length.";
			PassLen = LenCheck (reqType);
			Console.WriteLine ("Upper-Case Letters? (Yes = 0, No = 1)");
			UpCheck = BoolCheck ();
			Console.WriteLine ("Numbers? (Yes = 0, No = 1)");
			NumCheck = BoolCheck ();
			Console.WriteLine ("Special Characters? (Yes = 0, No = 1)");
			SpecCheck = BoolCheck ();
			FinalPass = Generate (PassLen, alph, alphUpper, spec, num, UpCheck, NumCheck, SpecCheck);
			Console.WriteLine ("Your randomly generated password is:");
			Console.WriteLine ("~~~~~~~~~~~~~~~~~~~~~~~~");
			Console.WriteLine (FinalPass);
			Console.WriteLine ("~~~~~~~~~~~~~~~~~~~~~~~~");
			Console.WriteLine ("Generate another password? (Yes = 0, No = 1");
			GenAgain = BoolCheck ();
			if (GenAgain == true) {
				Console.Clear ();
				goto Main;
			}
		}

		public static int LenCheck(string reqType) {
			int n;
			Loop:
			while (!int.TryParse(Console.ReadLine(), out n)) {
				Console.WriteLine("    Invalid entry. Only enter numbers for " + reqType);
			}
			if (n > 5) {
				return n;
			} else {
				Console.WriteLine ("    Invalid entry. Password must be at least 6 characters long.");
				goto Loop;
			}
		}

		public static bool BoolCheck() {
			int n;
			Loop:
			while (!int.TryParse(Console.ReadLine(), out n)) {
				Console.WriteLine("    You must enter either 0 for Yes or 1 for No.");
			}
			if (n == 0) {
				return true;
			} else if (n == 1) {
				return false;
			} else {
				Console.WriteLine("    You must enter either 0 for Yes or 1 for No.");
				goto Loop;
			}
		}

		public static string Generate(int PassLen, List<char> alph, List<char> alphUpper, List<char> spec, List<char> num, bool UpCheck, bool NumCheck, bool SpecCheck) {
			List<char> availChar = new List<char>();
			string[] passArr = new string[PassLen];
			Random ran = new Random();
			string pass;

			for (int i = 0; i < alph.Count; i++) {
				availChar.Add (alph [i]);
			}
			if (UpCheck == true) {
				for (int i = 0; i < alphUpper.Count; i++) {
					availChar.Add (alphUpper [i]);
				}
			}
			if (NumCheck == true) {
				for (int i = 0; i < num.Count; i++) {
					availChar.Add (num [i]);
				}
			}
			if (SpecCheck == true) {
				for (int i = 0; i < spec.Count; i++) {
					availChar.Add (spec [i]);
				}
			}

			for (int a = 0; a < PassLen; a++) {
				int ranNum = ran.Next (0, availChar.Count);
				passArr [a] = availChar [ranNum].ToString(); //Randomize code
			}
			pass = string.Join ("", passArr);
			return pass;
		}

	}
}
