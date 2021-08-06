#include <iostream>
#include <vector>

using namespace std;

string pig_it(string str);

int main(){

	string ans;

	ans = pig_it(",");
	cout << ans << endl;

	return 0;
}

string pig_it(string str){

	vector<string> splitWord;
	string word;
	string ans;

	for (auto &ch : str){
		
		if (ch == ' '){
			if (word == "!" || word == "." || word == "?"){
				splitWord.push_back(word);
			}else{
				word.push_back(word[0]);
				word.push_back('a');
				word.push_back('y');
				word.erase(0,1);
				splitWord.push_back(word);
			}
			word = "";
		} else{
			word += ch;
		}
	}
	if (word == "!" || word == "." || word == "?"){
				splitWord.push_back(word);
			}else{
				word.push_back(word[0]);
				word.push_back('a');
				word.push_back('y');
				word.erase(0,1);
				splitWord.push_back(word);
			}

	for (auto &ch : splitWord){
		ans += ch;
		ans += ' ';
	}
	ans.pop_back();

    return ans;
}












