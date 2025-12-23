/*
Simple CLI Greeting Program
Demonstrates basic Rust syntax, input handling, and functions.
*/

use std::io;

fn main() {
    println!("Enter your name:");

    let mut name = String::new();
    io::stdin()
        .read_line(&mut name)
        .expect("Failed to read input");

    let name = name.trim();
    greet(name);
}

fn greet(name: &str) {
    println!("Hello, {}! Welcome to Rust.", name);
}
