# Functional Decomposition

## Getting food from a vending machine

### Vending machine from a human perspective (in-class example)

You get a bag of chips from a vending machine.
- Approach machine
    - Walk until you are within arms reach
- Determine the number for the flavour I want.
    - Search for the specific flavour
    - Look just below it for the ID number. (Remember that number)
- Put in appropriate amount of money.
    - Look beside the ID number for the cost of the snack
    - Get out some money greater or equal to that amount.
    - Place that money into the intake.
- Key in the number for the flavour.
- Get bag from bottom of machine.
    - Bend down
    - Put arm through slot
    - Grab chips
    - Pull your arm out (with the chips)

### Vending machine from the machine's perspective -

You vend a bag of chips to a human.
- Wait for human to put in money
    - Give instructions to human to insert money into machine.
    - Accept the human's bill(s)/coin(s) through their designated slots.
    - Scan money for validity.
    - If money is valid, organize bills/coins individually into their specific storage compartments based on their type/amount.
    - Else, reject invalid bill from slot or drop invalid coins into the change compartment.
- Wait for human to key in item ID number.
    - After money is accepted, instruct human to key in their desired item's ID number.
    - If amount of money is insufficient for the chosen item, inform human of the insufficiency.
    - If item is out of stock, inform human that item is out of stock.
    - Else, proceed to process transaction.
- Refer to ID number and push bag of chips over the edge.
    - Activate rotating spring in the keyed-in ID number's slot.
    - Repeat 360 degree rotations until chip bag falls into retrieval compartment.
- Wait for human to retrieve bag from slot.
    - After chip bag is dropped, thank human and tell human to have a nice day.
    - Then, prepare instructions again for the next human to put in money.

### Identify where there might be basic programming concepts in your break-down.

- Displaying instructions may require simple commands that make certain pixels light up and/or move right to left for longer sentences.
- Displaying instructions may require a loop that will stop/change once the instructions are followed.
- Ensuring that the money is valid may require an if/else statement.
- Ensuring that the money is sufficient may also require an if/else statement.
- Organizing the change/bills into their individually organized slots may require if/else statements.
- Checking to see that the desired item is still in stock may also require an if/else statement.
- The rotating spring may require a simple command to rotate clockwise/counter clockwise.
- The rotating spring may require a loop that will stop rotations when the chip bag successfully falls into the retrieval slot.


###
    

    (Tip: focus on steps, pick one way of doing things and break down the steps, doesn't have to be practical, just functional)
