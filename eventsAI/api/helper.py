"""REST API for posts."""
import hashlib
import eventsAI


def check_login(username, password):
    """Check Authentication."""
    connection = eventsAI.model.get_db()

    print(password)

    if len(password) == 0:
        return "fail"
    if len(username) == 0:
        return "fail"

    cur = connection.execute(
        "SELECT * "
        "FROM users WHERE users.username = ?",
        (username, )
    )
    result = cur.fetchone()
    if result is not None:

        algorithm = 'sha512'
        correct_pass = result['password']

        parts = correct_pass.split('$')
        # print(parts)
        salt = parts[1]
        correct_hash = parts[2]

        password_salted = salt + password
        hash_obj = hashlib.new(algorithm)
        hash_obj.update(password_salted.encode('utf-8'))
        password_hash = hash_obj.hexdigest()

        if password_hash == correct_hash:
            return "success"
        return "fail"
    return "fail"
