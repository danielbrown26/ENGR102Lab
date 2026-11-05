# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:  TYLER BAKER
#.       DANIEL BROWN
#        WILLIAM SCHOENNBERGER
#        NOAH DOUGHERTY
# Section: 571
# Assignment: Lab 10 team
# Date: 3 November 2026


# chocolate_boxes.py

import random
import time


def _normalize_text(value):
    """Lowercase text and collapse repeated whitespace."""

    if value is None:
        return ""

    return " ".join(str(value).strip().lower().split())


def _normalize_truffle(values):
    """
    Normalize a truffle description to:

    (chocolate type, shape, filling, topping)
    """

    if not isinstance(values, (list, tuple)) or len(values) != 4:
        return None

    chocolate = _normalize_text(values[0])
    shape = _normalize_text(values[1])
    filling = _normalize_text(values[2])
    topping = _normalize_text(values[3])

    chocolate_aliases = {
        "dark chocolate": "dark",
        "milk chocolate": "milk",
        "white chocolate": "white",
    }

    shape_aliases = {
        "heart shaped": "heart",
        "round shaped": "round",
        "square shaped": "square",
        "rectangle shaped": "rectangle",
        "rectangular": "rectangle",
    }

    filling_aliases = {
        "vanilla creme": "vanilla",
        "vanilla cream": "vanilla",
        "strawberry creme": "strawberry",
        "strawberry cream": "strawberry",
        "caramel creme": "caramel",
        "caramel cream": "caramel",
        "coconut creme": "coconut",
        "coconut cream": "coconut",
        "toffee creme": "toffee",
        "toffee cream": "toffee",
    }

    topping_aliases = {
        "": "none",
        "nothing": "none",
        "no topping": "none",
        "no toppings": "none",
        "no topping added": "none",
    }

    chocolate = chocolate_aliases.get(chocolate, chocolate)
    shape = shape_aliases.get(shape, shape)
    filling = filling_aliases.get(filling, filling)
    topping = topping_aliases.get(topping, topping)

    return chocolate, shape, filling, topping


def _prepare_truffles(chocolates):
    """
    Return a list of IDs and a dictionary of normalized descriptions.

    Returns (None, None) if input is malformed.
    """

    if not isinstance(chocolates, dict):
        return None, None

    ids = list(chocolates.keys())
    information = {}

    for truffle_id in ids:
        normalized = _normalize_truffle(chocolates[truffle_id])

        if normalized is None:
            return None, None

        information[truffle_id] = normalized

    return ids, information


def _pair_breaks_rule(first, second):
    """
    Return True if two normalized truffle descriptions cannot share a box.
    """

    chocolate_one, shape_one, filling_one, topping_one = first
    chocolate_two, shape_two, filling_two, topping_two = second

    # No two truffles with all four identical attributes in one box.
    if first == second:
        return True

    # Filling restrictions.
    if {filling_one, filling_two} == {"caramel", "vanilla"}:
        return True

    if {filling_one, filling_two} == {"toffee", "coconut"}:
        return True

    # Topping restrictions.
    if {topping_one, topping_two} == {"nuts", "sprinkles"}:
        return True

    if {topping_one, topping_two} == {
        "white chocolate drizzle",
        "dark chocolate drizzle",
    }:
        return True

    # Shape restrictions.
    if {shape_one, shape_two} == {"rectangle", "square"}:
        return True

    if {shape_one, shape_two} == {"round", "heart"}:
        return True

    return False


def _box_violation_count(box, information):
    """
    Return the number of broken rules in one box.

    A score of 0 means the box is valid.
    """

    if not isinstance(box, (list, tuple)) or len(box) != 4:
        return 1000

    if len(set(box)) != 4:
        return 1000

    try:
        truffles = [information[truffle_id] for truffle_id in box]
    except KeyError:
        return 1000

    violations = 0

    # Check all pairs of truffles in the box.
    for first_index in range(4):
        for second_index in range(first_index + 1, 4):
            if _pair_breaks_rule(
                truffles[first_index],
                truffles[second_index],
            ):
                violations += 1

    # White chocolate requirement:
    # Every box must contain 0, 2, or 3 white chocolate truffles.
    white_count = sum(
        truffle[0] == "white"
        for truffle in truffles
    )

    if white_count not in (0, 2, 3):
        violations += 1

    return violations


def check_boxes(chocolates, boxes):
    """
    Return True only when every truffle is used exactly once and every
    box follows all requirements.
    """

    ids, information = _prepare_truffles(chocolates)

    if ids is None:
        return False

    if len(ids) % 4 != 0:
        return False

    if not isinstance(boxes, list):
        return False

    if len(boxes) != len(ids) // 4:
        return False

    used_ids = []

    for box in boxes:
        if not isinstance(box, (list, tuple)):
            return False

        if len(box) != 4:
            return False

        if _box_violation_count(box, information) != 0:
            return False

        used_ids.extend(box)

    # Every input truffle ID must be used once and only once.
    if len(used_ids) != len(ids):
        return False

    if len(set(used_ids)) != len(ids):
        return False

    if set(used_ids) != set(ids):
        return False

    return True


def make_boxes(chocolates, time_limit=4):
    """
    Create boxes of four truffles.

    Searches for a valid arrangement for up to time_limit seconds.

    If a valid arrangement is found:
        Return it immediately.

    If time runs out:
        Return the complete arrangement found with the fewest violations.

    Return [] only if:
    - the number of truffles is not divisible by four;
    - the input is malformed.
    """

    ids, information = _prepare_truffles(chocolates)

    if ids is None:
        return []

    total_truffles = len(ids)

    if total_truffles == 0:
        return []

    if total_truffles % 4 != 0:
        return []

    number_of_boxes = total_truffles // 4

    try:
        time_limit = float(time_limit)
    except (TypeError, ValueError):
        time_limit = 4.0

    if time_limit < 0:
        time_limit = 0.0

    deadline = time.monotonic() + time_limit
    rng = random.Random()

    white_ids = []
    non_white_ids = []

    for truffle_id in ids:
        if information[truffle_id][0] == "white":
            white_ids.append(truffle_id)
        else:
            non_white_ids.append(truffle_id)

    def make_white_layout():
        """
        Return a random list of white-truffle counts for each box.

        Each count is 0, 2, or 3.

        Return None if the total number of white truffles cannot satisfy
        the white-chocolate rule globally.
        """

        white_total = len(white_ids)

        possible = [
            [False] * (white_total + 1)
            for _ in range(number_of_boxes + 1)
        ]

        possible[0][0] = True

        for box_number in range(1, number_of_boxes + 1):
            for total_so_far in range(white_total + 1):
                for white_in_box in (0, 2, 3):
                    previous_total = total_so_far - white_in_box

                    if (
                        previous_total >= 0
                        and possible[box_number - 1][previous_total]
                    ):
                        possible[box_number][total_so_far] = True

        if not possible[number_of_boxes][white_total]:
            return None

        layout = []
        remaining_whites = white_total

        for boxes_left in range(number_of_boxes, 0, -1):
            choices = []

            for white_in_box in (0, 2, 3):
                previous_total = remaining_whites - white_in_box

                if previous_total < 0:
                    continue

                if possible[boxes_left - 1][previous_total]:
                    choices.append(white_in_box)

            chosen_count = rng.choice(choices)
            layout.append(chosen_count)
            remaining_whites -= chosen_count

        rng.shuffle(layout)

        return layout

    def make_starting_arrangement():
        """
        Build a complete random arrangement.

        If possible, it begins with a valid 0/2/3 white-chocolate count
        in every box. The later swap search improves the other constraints.
        """

        white_layout = make_white_layout()

        shuffled_whites = white_ids[:]
        shuffled_non_whites = non_white_ids[:]

        rng.shuffle(shuffled_whites)
        rng.shuffle(shuffled_non_whites)

        boxes = []

        # Build a starting arrangement with legal white counts when possible.
        if white_layout is not None:
            white_position = 0
            non_white_position = 0

            for white_needed in white_layout:
                box = []

                for _ in range(white_needed):
                    box.append(shuffled_whites[white_position])
                    white_position += 1

                for _ in range(4 - white_needed):
                    box.append(shuffled_non_whites[non_white_position])
                    non_white_position += 1

                rng.shuffle(box)
                boxes.append(box)

            return boxes

        # If a legal white distribution is impossible, still make a complete
        # arrangement. It may not be valid, but it can be returned as the
        # best arrangement found if time expires.
        shuffled_ids = ids[:]
        rng.shuffle(shuffled_ids)

        for start in range(0, total_truffles, 4):
            boxes.append(shuffled_ids[start:start + 4])

        return boxes

    best_boxes = None
    best_score = None

    # Always create and evaluate one complete arrangement, even if the
    # requested time_limit is zero.
    first_restart = True

    while first_restart or time.monotonic() < deadline:
        first_restart = False

        boxes = make_starting_arrangement()

        scores = [
            _box_violation_count(box, information)
            for box in boxes
        ]

        current_score = sum(scores)

        if best_score is None or current_score < best_score:
            best_score = current_score
            best_boxes = [box[:] for box in boxes]

        if current_score == 0:
            return boxes

        # Improve this full arrangement until the deadline.
        while time.monotonic() < deadline:
            bad_boxes = [
                box_index
                for box_index in range(number_of_boxes)
                if scores[box_index] > 0
            ]

            if not bad_boxes:
                if check_boxes(chocolates, boxes):
                    return boxes
                break

            # Select an invalid box, preferring boxes with more violations.
            weights = [scores[index] for index in bad_boxes]

            first_box_index = rng.choices(
                bad_boxes,
                weights=weights,
                k=1,
            )[0]

            best_change = None
            best_moves = []

            # Look at a random set of possible swaps. A swap always keeps
            # all boxes at exactly four truffles and uses all IDs exactly once.
            for _ in range(200):
                first_position = rng.randrange(4)

                second_box_index = rng.randrange(number_of_boxes)

                while second_box_index == first_box_index:
                    second_box_index = rng.randrange(number_of_boxes)

                second_position = rng.randrange(4)

                old_pair_score = (
                    scores[first_box_index]
                    + scores[second_box_index]
                )

                first_candidate = boxes[first_box_index][:]
                second_candidate = boxes[second_box_index][:]

                first_candidate[first_position], second_candidate[second_position] = (
                    second_candidate[second_position],
                    first_candidate[first_position],
                )

                new_pair_score = (
                    _box_violation_count(first_candidate, information)
                    + _box_violation_count(second_candidate, information)
                )

                change = new_pair_score - old_pair_score

                if best_change is None or change < best_change:
                    best_change = change
                    best_moves = [
                        (
                            second_box_index,
                            first_candidate,
                            second_candidate,
                        )
                    ]

                elif change == best_change:
                    best_moves.append(
                        (
                            second_box_index,
                            first_candidate,
                            second_candidate,
                        )
                    )

            if not best_moves:
                continue

            # Prefer improvements. Sometimes accept neutral or worse swaps
            # to avoid getting trapped in a local minimum.
            accept_move = False

            if best_change < 0:
                accept_move = True
            elif best_change == 0:
                accept_move = rng.random() < 0.30
            else:
                accept_move = rng.random() < 0.03

            if not accept_move:
                continue

            (
                second_box_index,
                first_candidate,
                second_candidate,
            ) = rng.choice(best_moves)

            old_pair_score = (
                scores[first_box_index]
                + scores[second_box_index]
            )

            boxes[first_box_index] = first_candidate
            boxes[second_box_index] = second_candidate

            scores[first_box_index] = _box_violation_count(
                boxes[first_box_index],
                information,
            )

            scores[second_box_index] = _box_violation_count(
                boxes[second_box_index],
                information,
            )

            current_score += (
                scores[first_box_index]
                + scores[second_box_index]
                - old_pair_score
            )

            if current_score < best_score:
                best_score = current_score
                best_boxes = [box[:] for box in boxes]

            if current_score == 0:
                if check_boxes(chocolates, boxes):
                    return boxes

    # Time expired: return the complete grouping with the fewest violations.
    if best_boxes is None:
        return []

    return best_boxes


# ---------------------------------------------------------------------
# Small test
# ---------------------------------------------------------------------
if __name__ == "__main__":
    sample_chocolates = {
        1: ["white", "round", "caramel", "none"],
        2: ["white", "round", "strawberry creme", "nuts"],
        3: ["milk", "round shaped", "caramel", "white chocolate drizzle"],
        4: ["milk", "round", "strawberry", "none"],
        5: ["dark", "square", "toffee", "none"],
        6: ["milk", "square shaped", "caramel", "nuts"],
        7: ["dark", "square", "strawberry", "dark chocolate drizzle"],
        8: ["milk", "square", "caramel creme", "none"],
    }

    boxes = make_boxes(sample_chocolates, time_limit=2)

    print("Boxes:", boxes)
    print("Valid:", check_boxes(sample_chocolates, boxes))