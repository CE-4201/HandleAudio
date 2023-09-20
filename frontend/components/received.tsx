import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View } from "react-native";

export default function Received({ message }: { message: string }) {
  return (
    <View style={styles.container}>
      <View style={styles.transcribeContainer}>
        <Text style={styles.text}>{message}</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  text: {
    fontWeight: "600",
    fontSize: 16,
    color: "white",
  },
  container: {
    backgroundColor: "#fff",
    justifyContent: "flex-start",
    marginRight: 16,
    marginTop: 16,
  },
  transcribeContainer: {
    backgroundColor: "rgba(80, 0, 80, 0.4)",
    alignSelf: "flex-end",
    maxWidth: "75%",
    padding: 16,
    borderTopLeftRadius: 10,
    borderTopRightRadius: 10,
    borderBottomLeftRadius: 10,
  },
});
