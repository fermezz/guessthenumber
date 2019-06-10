// External crate
#[macro_use]
extern crate text_io;

// Internal modules
mod game;

const GAME_OVER_MESSAGE: &str = "Game over! Hope you had fun :)";


fn main() -> std::io::Result<()> {
    println!("Hey there! There are two games to play here:
    \t1. Machine guesses, you think
    \t2. You guess, machine thinks");

    let _i: i32 = try_read!().expect("Must provide a number.");

    game::play().unwrap();

    println!("{}", GAME_OVER_MESSAGE);
    Ok(())
}
