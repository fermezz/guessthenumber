extern crate rand;


pub struct Answer {
    rights: u8,
    wrongs: u8,
    present_but_wrong: u8
}

impl Answer {
    pub fn is_correct(&self, guess: String) -> bool {
        self.rights == guess.len() as u8
        && self.wrongs == 0
        && self.present_but_wrong == 0
    }
}

pub fn evaluate_guess(guess: &str, number: String) -> Answer {
    let mut rights: u8 = 0;
    let mut wrongs: u8 = 0;
    let mut present_but_wrong: u8 = 0;

    let mut iterable_number = number.chars();

    for c in guess.chars()
    {
        let is_right: bool = c == iterable_number.next().unwrap();
        let is_present: bool = number.contains(c);

        match (is_right, is_present) {
            (false, false) => wrongs += 1,
            (false, true)  => present_but_wrong += 1,
            (true, _)      => rights += 1,
        }
    };

    Answer { rights, wrongs, present_but_wrong }
}
