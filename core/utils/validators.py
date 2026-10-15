from math import isfinite
from numbers import Real


REQUIRED_FEATURES = (
    "total_click",
    "early_click",
    "early_active_days",
    "first_activity_day",
    "pre_course_engaged",
)


def validate_input(student_dict):
    if not isinstance(student_dict, dict):
        raise TypeError("student_input must be a dictionary")

    missing_features = [feature for feature in REQUIRED_FEATURES if feature not in student_dict]
    if missing_features:
        raise ValueError(f"Missing required features: {', '.join(missing_features)}")

    for feature in REQUIRED_FEATURES:
        value = student_dict[feature]
        if value is None:
            continue
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError(f"{feature} must be a number or None")
        if not isfinite(value):
            raise ValueError(f"{feature} must be finite")
