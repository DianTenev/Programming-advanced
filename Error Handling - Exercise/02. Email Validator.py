class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


current_email = input()
domains = [".com", ".bg", ".org", ".net"]

while current_email != "End":
    name = current_email.split("@")[0]
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if "@" not in current_email:
        raise MustContainAtSymbolError("Email must contain @")

    for current_domain in domains:
        if current_domain in current_email:
            break
    else:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
    current_email = input()




