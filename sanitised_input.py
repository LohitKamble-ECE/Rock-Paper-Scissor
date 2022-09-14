def sanitised_input(
    prompt, type_expected=None, minimum=None, maximum=None, choices=None
):
    # Validating minimum < maximum
    if minimum is not None and maximum is not None and maximum < minimum:
        raise ValueError("minimum must be less than or equal to maximum.")

    # Getting user response
    user_response = input(prompt)

    # Validating reponse type
    if type_expected is not None:
        try:
            user_response = type_expected(user_response)
        except ValueError:
            raise TypeError(f"Input type must be {type_expected.__name__}.")

    # Validating response limit (upper and lower)
    if maximum is not None and user_response > maximum:
        raise ValueError(f"Input must be less than or equal to {maximum}.")
    elif minimum is not None and user_response < minimum:
        raise ValueError(f"Input must be greater than or equal to {minimum}.")
    elif choices is not None and user_response not in choices:
        if isinstance(choices, range):
            raise ValueError(
                f"Input must be between {choices.start} and {choices.stop}."
            )
        else:
            if len(choices) == 1:
                raise ValueError(f"Input must be {choices[0]}.")
            else:
                raise ValueError(
                    f"Input must be {' or '.join((', '.join(str(x) for x in choices[:-1]), str(choices[-1])))}."
                )
    else:
        return user_response
