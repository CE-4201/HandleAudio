import React, { useState, useEffect } from "react";
import { Pressable, StyleSheet, View } from "react-native";
import Icon from "react-native-vector-icons/FontAwesome";
import Loading from "./loading";
import messagesData from "../assets/messages.json";

interface MessageType {
  type: string;
  message: string;
}

export default function Mic() {
  const [iconType, setIconType] = useState("microphone");
  const [isTranscribeLoading, setIsTranscribeLoading] = useState(false);
  const [isChatGPTLoading, setIsChatGPTLoading] = useState(false);

  const [messages, setMessages] = useState<MessageType[]>([]);

  useEffect(() => {
    setMessages(messagesData);
    if (
      messages.length > 0 &&
      messages[messages.length - 1].type === "transcribed"
    ) {
      setIsChatGPTLoading(true);
    } else {
      setIsChatGPTLoading(false);
    }
  }, [messagesData]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "d") {
        setIconType("none");
      } else if (e.key === "Enter" && iconType === "send") {
        setIsTranscribeLoading(true);
        setIconType("microphone");
      }
    };

    const handleKeyUp = (e: KeyboardEvent) => {
      if (e.key === "d" && iconType === "none") {
        setIconType("send");
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    window.addEventListener("keyup", handleKeyUp);

    return () => {
      window.removeEventListener("keydown", handleKeyDown);
      window.removeEventListener("keyup", handleKeyUp);
    };
  }, [iconType]);

  return (
    <View style={styles.container}>
      {isTranscribeLoading && <Loading align="left" />}
      {isChatGPTLoading && <Loading align="right" />}
      <Pressable style={styles.button}>
        {iconType === "microphone" && (
          <Icon name="microphone" size={50} color={"white"} />
        )}
        {iconType === "none" && <View style={styles.stop} />}
        {iconType === "send" && <Icon name="send" size={50} color={"white"} />}
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  stop: {
    width: 35,
    height: 35,
    borderRadius: 10,
    backgroundColor: "white",
  },
  container: {
    width: "100%",
    alignItems: "center",
    justifyContent: "center",
  },
  button: {
    backgroundColor: "rgba(40, 0, 168, 0.4)",
    alignItems: "center",
    justifyContent: "center",
    width: 100,
    paddingVertical: 16,
    height: 100,
    borderRadius: 50,
  },
});
