// External crates
extern crate rand;

use rand::Rng;

pub fn generate_stringified_random_number(cipher_quantity: u8) -> String {
    let mut rng = rand::thread_rng();
    let mut thought_number: String = "".to_string();

    for _ in 1..=cipher_quantity
    {
        thought_number.push_str(&rng.gen_range(0, 10).to_string());
    }

    thought_number
}
