class BaseHandler:
  """
  Base handler class for JRAVIS streams.
  Each handler should override the run() method.
  """

  def run(self):
    raise NotImplementedError("Handler must implement run()")
