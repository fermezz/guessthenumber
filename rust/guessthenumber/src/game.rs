// Internal modules
mod evaluator;
mod common;


pub fn play() -> std::result::Result<(), Box<dyn std::error::Error>> {
    let thought_number = common::generate_stringified_random_number(4);
    println!("Thought number: {}", thought_number);
    let guess = ask_for_a_guess();

    let answer: evaluator::Answer = evaluator::evaluate_guess(&guess, thought_number);

    if answer.is_correct(guess)
    {
        println!("You win!");
    }
    else
    {
        println!("You lose!");
    }
    Ok(())
}



fn ask_for_a_guess() -> String {
    try_read!().unwrap()
}
