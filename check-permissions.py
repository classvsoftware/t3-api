#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "t3api_utils>=1.4.0",
# ]
# ///


from t3api_utils.api.operations import send_api_request
from t3api_utils.main.utils import get_authenticated_client_or_error, pick_license


def main():
    api_client = get_authenticated_client_or_error()

    license = pick_license(api_client=api_client)
    license_number = license["licenseNumber"]

    views = send_api_request(
        api_client,
        "/v2/permissions/views",
        params={"licenseNumber": license_number},
    )

    print(f"\nAvailable views for {license_number}:")
    for i, view in enumerate(views, 1):
        print(f"  {i}. {view}")

    choice = int(input("\nSelect a view: ")) - 1
    selected_view = views[choice]

    permissions = send_api_request(
        api_client,
        "/v2/permissions",
        params={"licenseNumber": license_number, "view": selected_view},
    )

    print(f"\nPermissions for '{selected_view}' on {license_number}:")
    for perm in permissions:
        print(f"  - {perm}")


if __name__ == "__main__":
    main()
