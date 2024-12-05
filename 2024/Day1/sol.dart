import 'dart:io';
import 'dart:convert';
import 'dart:math';

int CalculateTotalDistance(List<int> l1, List<int> l2) {
	l1.sort();
	l2.sort();
	
	int distanceTotal = 0;
	for (var i = 0; i < l1.length; i++) {
		distanceTotal += max(l1[i], l2[i]) - min(l1[i], l2[i]).toInt();
	}

	return distanceTotal;
}

int GetOcc<T>(List<T> list, T n) {
  return list.where((elem) => elem == n).length;
}

int CalculateTotalSimilarity(List<int> l1, List<int> l2) {
  int similarityTotal = 0;

  for (var i = 0; i < l1.length; i++) {
    similarityTotal += l1[i] * GetOcc(l2, l1[i]);
  }
  
  return similarityTotal;
  
}
void main(List<String> args) {

	String contents_raw = File(args[0]).readAsStringSync(encoding: utf8);
	// List<List<String>> contents_str = contents_raw
	List<String> contents_str = contents_raw // "123    312\n 153   1232\n..."
		.split('\n') // ["123    312", " 153   1232", ..., " "]
		.map((line) => line.trim().split('   ')) // [["123", "312"], ["153", "1232"], ..., " "]
		.expand((pair) => pair) // ["123", "312", "153", "1232", ..., " "]
		.toList();
	contents_str.length--; //remove the empty str as last elem
	List<int> contents = contents_str
		.map((str) => int.parse(str))
		.toList();

	List<int> l1 = [];
	List<int> l2 = [];
	for (var i = 0; i < contents.length; i++) {
		if (i % 2 == 0) {
			l1.add(contents[i]);
		}
		else {
			l2.add(contents[i]);
		}
  }
	
	int distance = CalculateTotalDistance(l1, l2);
  int similarity = CalculateTotalSimilarity(l1, l2);
	print('distance = ${distance}');
  print('similarity = ${similarity}');


}