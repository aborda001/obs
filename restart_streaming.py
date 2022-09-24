import obspython as obs


def script_description() -> str:
    return "Se puede habilitar o deshabilitar y configurar el tiempo de espera antes de iniciar la transmición"


def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_bool(props, "enabled", "Activo")
    obs.obs_properties_add_int_slider(
        props, "interval", "Intervalo en segundos", 20, 60, 1)
    return props


def check_stream(initial: bool = False) -> None:
    if not obs.obs_frontend_streaming_active():
        obs.obs_frontend_streaming_start()
        print('Restarted Stream!')


def script_update(settings) -> None:
    if obs.obs_data_get_bool(settings, "enabled"):
        print('Add timer!')
        obs.timer_add(
            check_stream,
            1 * obs.obs_data_get_int(settings, "interval") * 1000)
    else:
        print('Remove timer!')
        obs.timer_remove(check_stream)
