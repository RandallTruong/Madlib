def main():
    # Initialize variables
    adjective1 = input("Please enter an Adjective: ")
    adjective2 = input("Please enter another Adjective: ")
    bird = input("Please enter a bird: ")
    room = input("Please enter a room: ")
    verb_past_tense = input("Please enter a verb in past tense: ")
    verb = input("Please enter a verb: ")
    relative_name = input("Please enter a person's name: ")
    noun = input("Please enter a noun: ")
    liquid = input("Please enter a liquid: ")
    verb_ending_ing = input("Please enter a verb ending in ING: ")
    body_part_ = input("Please enter a body part: ")
    plural_noun = input("Please enter a plural noun: ")
    verb_ending_ing2 = input("Please enter another verb ending in ING: ")
    noun2 = input("Please enter one last noun: ")

    # Display paragraph
    print(f"It was {adjective1}, cold November day. I woke up to the {adjective2}"
          f" smell of {bird} roasting in the {room} downstairs. I {verb_past_tense} down the stairs"
          f" to see if I could help {verb} the dinner. My mom said, \"See if {relative_name} needs a fresh"
          f"{noun}.\" So I carried a tray of glasses full of {liquid} into the {verb_ending_ing} room. When I got there, I"
          f" could not believe my {body_part_}! There were {plural_noun} {verb_ending_ing2} on the {noun2}!")

    # Print entire paragraph
    pass


if __name__ == "__main__":
    main()
