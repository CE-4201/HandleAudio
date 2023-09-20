import React, { useEffect, useState } from "react";
import { StyleSheet, View, Text, Dimensions, FlatList } from "react-native";
import Transcribed from "./components/transcribed";
import Title from "./components/title";
import Received from "./components/received";
import messagesData from "./assets/messages.json";

interface MessageType {
  type: string;
  message: string;
}

const screenHeight = Dimensions.get("window").height;
export default function App() {
  const [messages, setMessages] = useState<MessageType[]>([]);

  useEffect(() => {
    setMessages(messagesData);
  }, [messagesData]);

  const renderItem = ({ item }: { item: MessageType }) => {
    if (item.type === "transcribed") {
      return <Transcribed message={item.message} />;
    } else {
      return <Received message={item.message} />;
    }
  };

  return (
    <View style={styles.container}>
      <Title />
      <FlatList
        style={styles.listContainer}
        data={messages}
        renderItem={renderItem}
        keyExtractor={(item, index) => index.toString()}
        showsVerticalScrollIndicator={false}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    paddingBottom: 16,
  },
  listContainer: {
    height: screenHeight - 56,
  },
});
