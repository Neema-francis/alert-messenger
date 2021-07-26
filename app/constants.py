# The below logics is for difffernt alert colors

status_danger = 'danger'
status_success = 'success'
status_info = 'info'
status_warning = 'warning'

STATUS = (
    (status_danger, 'Danger'),
    (status_success, 'Success'),
    (status_info, 'Info'),
    (status_warning, 'Warning')
)

alert_color = {
    status_danger: "alert alert-danger",
    status_success: "alert alert-success",
    status_info: "alert alert-info",
    status_warning: "alert alert-warning",
}