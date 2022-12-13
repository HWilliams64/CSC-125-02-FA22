def spill_it(drink=None):
    try:
        msg = f"I'll drink my {drink}" if drink else "There is nothing to drink"
        print(msg)

        if drink: 
            raise RuntimeError(f"I spilled the {drink}")
    except Exception as e:  # This is run when there is and Exception
        print(f"{e}.  Don't worry I'll get you another one!")
    else:# This is run when there is no error 
        print("Nothing happened here")
    finally:  # This is always run
        print("I am just here to clean up after everyone")

spill_it("coffee")