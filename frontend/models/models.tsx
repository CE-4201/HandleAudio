type MessageType = {
  type: "transcribed" | "received";
  message: string;
};
type TranscribedProps = {
  message: string;
};

type ReceivedProps = {
  message: string;
};
