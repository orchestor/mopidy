from mopidy import exceptions

try:
    import cherrypy
except ImportError as import_error:
    raise exceptions.OptionalDependencyError(import_error)


class ApiResource(object):
    def __init__(self, core):
        self.core = core

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        playback_state = self.core.playback.state.get()
        track = self.core.playback.current_track.get()
        if track:
            track = track.serialize()
        return {
            'playback_state': playback_state,
            'current_track': track,
        }
