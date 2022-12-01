use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let input = fs::read_to_string(&args[1])
        .expect("Should have been able to read the file");
    let mut calories: i32 = 0;
    let mut elves: Vec<i32> = Vec::new();
    for line in input.trim().split("\n").into_iter() {
        if line.trim().is_empty() {
            elves.push(calories);
            calories = 0;
            continue;
        }
        calories += line.parse::<i32>().unwrap();
    }
    elves.sort();
    elves.reverse();
    println!("{:?}", elves[0]);
    println!("{:?}", &elves[0..3].iter().sum::<i32>());
}