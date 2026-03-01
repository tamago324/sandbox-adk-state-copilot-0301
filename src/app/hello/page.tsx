"use client";

import { useAgent } from "@copilotkit/react-core/v2";
import { useState } from "react";

export default function HelloPage() {
  const [value, setValue] = useState("");

  const { agent } = useAgent({
    agentId: "my_agent",
  });

  const onClick = () => {
    agent.addMessage({
      id: crypto.randomUUID(),
      role: "user",
      content: `私の名前は${value}です！`,
    });
    agent.runAgent();
  };

  return (
    <div className="flex min-h-screen items-center justify-center">
      <div className="flex flex-col gap-4">
        <input
          type="text"
          value={value}
          onChange={(e) => setValue(e.target.value)}
          className="rounded border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400"
          placeholder="テキストを入力"
        />
        <button
          type="button"
          className="rounded bg-blue-500 px-4 py-2 text-white hover:bg-blue-600"
          onClick={onClick}
        >
          送信
        </button>

        <div className="mt-4 rounded border border-gray-300 bg-gray-100 p-4">
          {agent.isRunning ? (
            <p className="text-gray-700">エージェントが実行中...</p>
          ) : (
            <p className="text-gray-700">
              {agent.state.user_name
                ? `エージェントの応答: ${agent.state.user_name}`
                : "エージェントの応答がここに表示されます"}
            </p>
          )}
        </div>
      </div>
    </div>
  );
}
