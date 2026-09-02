from rag.search_phone import get_all_phones
import re


def get_cheapest_phone():

    phones = get_all_phones()

    cheapest_phone = None
    cheapest_price = float("inf")

    for phone in phones:

        try:

            price_text = str(phone["price"])

            # প্রথম USD price বের করবে
            match = re.search(r"\$[\s ]*([\d,.]+)", price_text)

            if match:

                price = match.group(1)
                price = price.replace(",", "")

                price = float(price)

                if price < cheapest_price:

                    cheapest_price = price
                    cheapest_phone = phone["name"]

        except:
            pass

    if cheapest_phone:

        return (
            f"Cheapest Samsung phone is "
            f"{cheapest_phone} "
            f"(Price: ${cheapest_price})"
        )

    return "Price information not available."


def get_best_battery_phone():

    phones = get_all_phones()

    best_phone = None
    best_battery = 0

    for phone in phones:

        try:

            battery_text = str(phone["battery"])

            match = re.search(r"(\d+)\s*mAh", battery_text)

            if match:

                battery = int(match.group(1))

                if battery > best_battery:

                    best_battery = battery
                    best_phone = phone["name"]

        except:
            pass

    if best_phone:

        return (
            f"{best_phone} has the largest battery "
            f"({best_battery} mAh)."
        )

    return "Battery information not available."